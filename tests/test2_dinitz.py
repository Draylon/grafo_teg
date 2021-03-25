def _BFS_using_levels(self, origin=None, goal=None):
    origin = origin or self.source
    goal = goal or self.sink

    self.level = [-1] * self.size
    self.level[origin] = 0

    to_visit = [origin]

    while to_visit:

        current = to_visit.pop(0)

        for successor in range(self.size):
            if self.capacity[(current, successor)] - self.flow[(current, successor)] > 0 and self.level[successor] < 0:
                self.level[successor] = self.level[current] + 1
                to_visit.append(successor)

    return self.level


def _send_flow(self, origin=None, goal=None, max_flow=float('inf')):

    goal = goal or self.sink
    origin = origin or self.source

    # sink reached
    if origin == goal:
        return max_flow

    # traverse all neighbors
    for successor in range(self.size):

        # if a viable edge, a positive residual and d(u)<d(v)
        if ((self.capacity[(origin, successor)] - self.flow[(origin, successor)] > 0)
                and (self.level[origin] + 1 == self.level[successor])):

            # finds the bounding flow
            current_flow = min(max_flow, self.capacity[(origin, successor)] - self.flow[(origin, successor)])

            path_flow = self._send_flow(successor, goal, current_flow)

            # if the flow is viable, update the path.
            if path_flow > 0:
                self.flow[(origin, successor)] += path_flow
                self.flow[(successor, origin)] -= path_flow

                return path_flow
    return 0


def _max_flow_search_D(self, origin=None, goal=None):
    # initialzing vars
    goal = goal or self.sink
    origin = origin or self.source
    total_flow = 0

    # while there is path on the residual graph
    while True:
        # finds the path using BFS and marks their reachability to the sink
        self.level = self._BFS_using_levels(origin, goal)

        # if reached sink
        if self.level[goal] < 0:
            return total_flow

        # using the above paths to compute flow
        while True:
            path_flow = self._send_flow(origin, goal)

            if path_flow == 0:
                break

            # incrementing flow
            total_flow += path_flow


def Dinic(self, origin=None, goal=None):
    return self._max_flow_search_D(origin=origin, goal=goal)