#! /bin/python

#  Smali2Java: Directly convert Smali source files to Java. Translated from
#  C# version by darkguy2008 at https://github.com/darkguy2008/smali2java
#  Copyright (C) 2015 Andrew Phillips <skeledrew@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Docstring template.
  
  Created:
   15-10-12
  Last Modified:
   n/a
   
  Params:
   n/a
  Return:
   n/a
  
  Notes:
   n/a
  History:
   n/a
  """
  
# Imports


### Functions

# SmaliEngine.cs:
'''
decompile smali code
  create a list to hold the lines
  parse [SmaliLine] each line and add to list if !null
indent smali
'''

# SmaliLine.cs:
'''
Parse
 discard empty lines and comments
 remove string if exists
 split by space to get tokens
 if 1st token starts with '.', ie. should be a directive
  ensure it is a directive [ParseAsDirective], do some stuff
 if starts with ':', should be a label
  set type and label text
 if !start with '.', should be an intruction
  ensure it's an instruction line [ParseAsInstruction], do stuff
 return parsing results
ParseAsDirective
 [handle class, super, implements, source, field, method, prologue, registers, line, end, param [, locals]]
  class
   SetModifiers
 
'''

### Tests


### Notes


### Main

# Program.cs:
# check for input & output file args
# use sample if no input, stdout if no output
# decompiles & indents smali code [SmaliEngine]