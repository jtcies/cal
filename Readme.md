todo:
- [x] find some generalizable way to add runs
    - I think the easiest way to do this is going to be to capture this in the 'inning status' logic. Then it can be added to game status add the end of each half-inning. 
    - maybe when we pop the end of the bases off, we can determine how many were true and count them? seems hacky but could work as a start.
- [x] capture game status logic
- [ ] add more at-bat outcomes
- [ ] clean up some of the design decisions, i.e. `at_bat` takes an `inning_status` as an input whereas `game` takes no input