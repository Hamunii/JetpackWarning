## 2.2.0

- Fixed warning meter not going full while maintaining steady high speed, causing jetpack to explode
- Removed a mostly unnecessary variable from the warning meter fill logic, which would cause sudden changes in the meter
	- Removed meter fill dampening due to it no longer being necessary, making the meter more responsive
- This project is now maintained by Hamunii. Previously maintained by klepticat

## 2.1.0

- Updated meter values to provide a clearer danger reading
	- Should make it easier to keep maintain high speeds without exploding
- Fixed critical warning sound working improperly
	- Before when a player first reached critical, the warning sound would play properly. However, toggling the jetpack while in critical would cause the warning sound to end and not reactivate
	- Now the warning sound will continue to play, even if you toggle the jetpack while in critical

## 2.0.1

- Fixed README example image to work on thunderstore

## 2.0.0

- Fixed multiplayer issues
	- Should now work properly in multiplayer, rather than just singleplayer
	- If you encounter any issues still, add an issue to the github repo

## 1.1.1

- Updated README

## 1.1.0

- Added critical warning sound
- Added colors to meter
	- The meter turns more red as it fills
- Added dampening to the meter's value to help make sudden changes look better

## 1.0.1

- Fixed dropped jetpacks overriding the fill meter

## 1.0.0

- Initial release