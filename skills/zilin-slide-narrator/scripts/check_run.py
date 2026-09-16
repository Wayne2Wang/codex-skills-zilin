#!/usr/bin/env python3
"""Check production gates; not an authorization or artifact-verification tool.

run.json fields used:
  source_sha256, script_sha256, settings_sha256: current nonempty fingerprints
  approvals: intake, native, sample records; each has approved: true and the
    same three fingerprints. A native approval may omit settings_sha256
    because final-voice changes do not invalidate the teaching script.
  slides: [{page, included, status}]; status verified means a checked download
  sample_pages: first two included pages, or explicit user-selected override
Use --stage sample before the first paid preview; --stage bulk before the rest.
"""
import argparse,json
from pathlib import Path

def check(run,stage):
 errors=[]
 for key in ('source_sha256','script_sha256','settings_sha256'):
  if not run.get(key):errors.append('Missing current '+key)
 slides=run.get('slides',[]);pages=[s.get('page') for s in slides]
 if not pages or len(pages)!=len(set(pages)):errors.append('Missing or duplicate slide mapping')
 included=[s['page'] for s in slides if s.get('included')]
 if not included:errors.append('No included slides')
 required=['intake','native']+(['sample'] if stage=='bulk' else [])
 for gate in required:
  a=run.get('approvals',{}).get(gate,{})
  if a.get('approved') is not True:errors.append('Approval required: '+gate);continue
  keys=('source_sha256','script_sha256') if gate=='native' else ('source_sha256','script_sha256','settings_sha256')
  # Intake confirms source/settings; the script is created afterward.
  if gate=='intake':keys=('source_sha256','settings_sha256')
  for key in keys:
   if a.get(key)!=run.get(key):errors.append('Stale '+gate+' approval: '+key)
 if stage=='bulk':
  samples=run.get('sample_pages',included[:2])
  if not samples or any(p not in included for p in samples):errors.append('Invalid sample pages')
  for p in samples:
   if next((s.get('status') for s in slides if s['page']==p),None) not in ('verified','assembled'):
    errors.append('Sample audio not verified: '+str(p))
 return errors

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('run',type=Path);p.add_argument('--stage',choices=['sample','bulk'],required=True);args=p.parse_args()
 errors=check(json.loads(args.run.read_text()),args.stage)
 print(json.dumps({'ok':not errors,'stage':args.stage,'errors':errors},indent=2))
 raise SystemExit(bool(errors))
if __name__=='__main__':main()
