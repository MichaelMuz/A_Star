def lineOfSight(p0, p1, obstacleGrid):
    f = 0
    sy = 1
    sx = 1
    y0,x0 = p0
    y1,x1 = p1
    dy = y1 - y0
    dx = x1 - x0
    
    if dy < 0:
        dy = -dy
        sy = -1

    if dx < 0:
        dx = -dx
        sx = -1

    if dx >= dy:
        while x0 != x1:
            f = f + dy
            if f >= dx:
                if (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in obstacleGrid:
                    return False
                y0 = y0 + sy
                f = f - dx
            if f != 0 and (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in obstacleGrid:
                return False
            if dy == 0 and (int(x0 + ((sx - 1) / 2)), y0) in obstacleGrid and (int(x0 + ((sx - 1) / 2)),y0 - 1) in obstacleGrid:
                return False
            x0 = x0 + sx
    else:
        while y0 != y1:
            f = f + dx
            if f >= dy:
                if (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in obstacleGrid:
                    return False
                x0 = x0 + sx
                f = f - dy
            if f != 0 and (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in obstacleGrid:
                return False
            if dx == 0 and (x0, int(y0 + ((sy - 1) / 2))) in obstacleGrid and (x0 - 1, int(y0 + ((sy - 1) / 2))) in obstacleGrid:
                return False
            y0 = y0 + sy
    return True
