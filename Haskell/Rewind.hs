module Rewind where

import Data.List

rewind :: [a] -> [a]
rewind [] = []
rewind [x] = [x]
rewind (x:y) = rewind y ++ [x]