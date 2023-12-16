## Building

Place Lethal Company's `Assembly-CSharp.dll`, as well as `UnityEngine.CoreModule.dll`, `UnityEngine.UI.dll`, and `Unity.Netcode.Runtime.dll` in the `dlls/` folder.

These can be found in the `Lethal Company/Lethal Company_Data/Managed/` folder.

## Making a Thunderstore Package

Run MakeRelease.py to make a zip file which contains the necessary files for a thunderstore package. That script has only been tested on Linux, but it should probably work on Windows too. Make sure to make a release build first though, so it can get the dll file.