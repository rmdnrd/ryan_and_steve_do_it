package main

import (
	depthfinder "aoc/01"
	"aoc/inputs"
)

func errorCheck(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	depthfinder.GetdepthIncreaseCount(inputs.DepthFinderInputs)
	depthfinder.GetDepthSumIncreaseCount(inputs.DepthFinderInputs)
}
