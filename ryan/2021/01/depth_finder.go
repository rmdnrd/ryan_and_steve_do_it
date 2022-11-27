package depthfinder

import "fmt"

func errorCheck(e error) {
	if e != nil {
		panic(e)
	}
}

/*
count the number of times a depth measurement increases from the previous measurement.
(There is no measurement before the first measurement.)
*/
func GetdepthIncreaseCount(inputs []int) {
	count := 0
	for i := 0; i < len(inputs); i++ {
		if i == 0 {
			continue
		}
		previousDepth := inputs[i-1]
		currentDepth := inputs[i]
		if currentDepth > previousDepth {
			count++
		}
	}

	fmt.Printf("Solution 1 answer: %d\n", count)
}

/*
count the number of times the sum of measurements in this sliding window increases from the previous sum.
So, compare A with B, then compare B with C, then C with D, and so on.
Stop when there aren't enough measurements left to create a new three-measurement sum.
*/
func GetDepthSumIncreaseCount(inputs []int) {
	count := 0
	previousSum := 0
	for i := 0; i < len(inputs)-2; i++ {
		if i == 0 {
			previousSum = inputs[i] + inputs[i+1] + inputs[i+2]
			continue
		}
		currentSum := inputs[i] + inputs[i+1] + inputs[i+2]

		if currentSum > previousSum {
			count++
		}
		previousSum = currentSum
	}

	fmt.Printf("Solution 2 answer: %d\n", count)
}
