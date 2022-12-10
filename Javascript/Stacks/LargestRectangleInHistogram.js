function largestRectangleArea(heights) {
  // Create a stack to keep track of the bars in the histogram
  const stack = [];

  // Add a zero-height bar at the end of the array to make sure all bars in the stack get popped
  heights.push(0);

  let maxArea = 0;
  let i = 0;
  while (i < heights.length) {
    // If the current bar is taller than the bar on the top of the stack, push it onto the stack
    if (stack.length === 0 || heights[i] > heights[stack[stack.length - 1]]) {
      stack.push(i);
      i += 1;
    } else {
      // If the current bar is shorter than the bar on the top of the stack, pop the top bar from the stack
      const top = stack.pop();

      // Calculate the area of the rectangle formed by the popped bar
      const area =
        heights[top] * (stack.length === 0 ? i : i - stack.length - 1);

      // Update the maximum area if necessary
      maxArea = Math.max(maxArea, area);
    }
  }

  return maxArea;
}
