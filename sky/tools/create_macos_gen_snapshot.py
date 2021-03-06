#!/usr/bin/env python
# Copyright 2013 The Flutter Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import subprocess
import sys
import os


def main():
  parser = argparse.ArgumentParser(description='Creates multi-arch gen_snapshot')

  parser.add_argument('--dst', type=str, required=True)
  parser.add_argument('--arm64-out-dir', type=str, required=True)
  parser.add_argument('--armv7-out-dir', type=str, required=True)

  args = parser.parse_args()

  fat_gen_snapshot = os.path.join(args.dst, 'gen_snapshot')
  arm64_gen_snapshot = os.path.join(args.arm64_out_dir, 'clang_x64', 'gen_snapshot')
  armv7_gen_snapshot = os.path.join(args.armv7_out_dir, 'clang_x86', 'gen_snapshot')

  if not os.path.isfile(arm64_gen_snapshot):
    print 'Cannot find x86_64 (arm64) gen_snapshot at', arm64_gen_snapshot
    return 1

  if not os.path.isfile(armv7_gen_snapshot):
    print 'Cannot find i386 (armv7) gen_snapshot at', armv7_gen_snapshot
    return 1

  subprocess.check_call([
    'lipo',
    arm64_gen_snapshot,
    armv7_gen_snapshot,
    '-create',
    '-output',
    fat_gen_snapshot,
  ])


if __name__ == '__main__':
  sys.exit(main())

