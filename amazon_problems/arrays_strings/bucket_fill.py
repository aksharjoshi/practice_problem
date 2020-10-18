## Given a 2D array of image pixel values, implement the bucket fill feature used in various image editing softwares.
## The bucket fill takes a single pixel location (x, y) that was clicked and changes the color of that location.
## This is repeated for each neighbor that has the same original color of the starting pixel.
## It ends when there are no more neighbors that have the original color.

##bucket_fill(int[][] image, int clickX, int clickY, int newColor);
##  [1,  1,  1,  1],
##  [1,  1,  2,  2],
##  [1,  2,  2,  2],
##  [2,  1,  1,  2],
##  [2,  1,  3,  2]

##Click on (3, 0) with color 3

##[3, 3, 3, 3],
##[3, 3, 2, 2],
##[3, 2, 2, 2],
##[2, 1, 1, 2],
##[2, 1, 3, 2]
##- Indexes are zero-indexed, left-right, top-bottom
##- Neighbors are defined as adjacent cells to the left, right, top, and bottom of a given cell. No diagonals.
##- dimensions of image are NxM
def bucket_fill_helper(image, clickX, clickY, newColor):
    oldColor = image[clickX][clickY]
    bucket_fill_helper(image, clickX, clickY, newColor, oldColor)

def bucket_fill_helper(image, clickX, clickY, newColor, oldColor):
    #to return empty bucket
    if not image:
        return image
    
    #base case
    if clickX < 0 or clickX >= len(image[0]) or clickY < 0 or clickY >= len(image[0]) or image[clickX][clickY] != oldColor:
        return
    
    image[clickX][clickY] = newColor
    bucket_fill_helper(image, clickX, clickY +1, oldColor)
    bucket_fill_helper(image, clickX, clickY -1, oldColor)
    bucket_fill_helper(image, clickX+1, clickY, oldColor)
    bucket_fill_helper(image, clickX-1, clickY, oldColor)