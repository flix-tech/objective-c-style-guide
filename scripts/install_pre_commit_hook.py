#!/usr/bin/python

'''
The MIT License (MIT)
Copyright (c) 2015-present Badoo Trading Limited.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
 
import os
import platform
import shutil

git_hooks_dir = os.path.abspath(os.path.join(os.getcwd(), '.git/hooks'))
if not os.path.exists(git_hooks_dir):
    print 'Created', git_hooks_dir
    os.makedirs(git_hooks_dir)

pre_commit_hook_dst = os.path.join(git_hooks_dir, 'pre-commit')
if os.path.islink(pre_commit_hook_dst) or os.path.isfile(pre_commit_hook_dst):
    print 'Removed previously installed hook'
    os.remove(pre_commit_hook_dst)

scripts_dir = os.path.split(os.path.abspath(__file__))[0]
    
pre_commit_hook_src = os.path.join(scripts_dir,   'pre_commit.py')
if platform.system() == 'Windows':
	shutil.copy(pre_commit_hook_src, pre_commit_hook_dst)
	print 'Installed git hook into', pre_commit_hook_dst
else:
	os.symlink(pre_commit_hook_src, pre_commit_hook_dst)
	print 'Installed git hook into', pre_commit_hook_dst, '~>', pre_commit_hook_src
