from py_wikiracer.internet import Internet
from typing import List

class Parser:

    @staticmethod
    def get_links_in_page(html: str) -> List[str]:
        """
        In this method, we should parse a page's HTML and return a list of links in the page.
        Be sure not to return any link with a DISALLOWED character.
        All links should be of the form "/wiki/<page name>", as to not follow external links
        """
        links = []
        disallowed = Internet.DISALLOWED

        # YOUR CODE HERE
        substr = "href=\"/wiki/"
        match_find = [link for link in range(len(html)) if html.startswith(substr, link)]

        # href="/wiki/*" match this regex, append to links
        possible_links = []
        for link in match_find:
            possible_links.append(html[link+6:html.find('\"',link+6)])

        # remove duplicates
        for link in possible_links:
            if link not in links:
                links.append(link)

        # filter links using disallowed chars
        remove_links = []
        for i in range(len(links)):
            for char in disallowed:
                if links[i].find(char,6) != -1:
                    remove_links.append(links[i])
                    break

        # remove invalid links
        for link in remove_links:
            links.remove(link)

        # You can look into using regex, or just use Python's find methods to find the <a> tags or any other identifiable features
        # A good starting place is to print out `html` and look for patterns before/after the links that you can string.find().
        # Make sure your list doesn't have duplicates. Return the list in the same order as they appear in the HTML.
        # This function will be stress tested so make it efficient!

        return links

# In these methods, we are given a source page and a goal page, and we should return
#  the shortest path between the two pages. Be careful! Wikipedia is very large.

# These are all very similar algorithms, so it is advisable to make a global helper function that does all of the work, and have
#  each of these call the helper with a different data type (stack, queue, priority queue, etc.)

class BFSProblem:
    def __init__(self):
        self.internet = Internet()
    # Example in/outputs:
    #  bfs(source = "/wiki/Computer_science", goal = "/wiki/Computer_science") == ["/wiki/Computer_science", "/wiki/Computer_science"]
    #  bfs(source = "/wiki/Computer_science", goal = "/wiki/Computation") == ["/wiki/Computer_science", "/wiki/Computation"]
    # Find more in the test case file.

    # Do not try to make fancy optimizations here. The autograder depends on you following standard BFS and will check all of the pages you download.
    # Links should be inserted into the queue as they are located in the page, and should be obtained using Parser's get_links_in_page.
    # Be very careful not to add things to the "visited" set of pages too early. You must wait for them to come out of the queue first. See if you can figure out why.
    #  This applies for bfs, dfs, and dijkstra's.
    # Download a page with self.internet.get_page().
    def bfs(self, source = "/wiki/Calvin_Li", goal = "/wiki/Wikipedia"):
        path = [source]

        # YOUR CODE HERE
        # ...
        path_exist = False
        queue = []
        seen = []
        queue.append(path)

        while queue:
            path = queue.pop(0)
            path_end = path[-1]
            
            if path_end not in self.internet.requests:
                html = self.internet.get_page(path_end)
                links = Parser().get_links_in_page(html)

                if goal in links:
                    path_exist = True
                    path.append(goal)
                    return path

                for link in links:
                    if link not in seen:
                        new_path = list(path)
                        new_path.append(link)
                        queue.append(new_path)
                        seen.append(link)

        if path_exist == False:
            return None # if no path exists, return None

class DFSProblem:
    def __init__(self):
        self.internet = Internet()
    # Links should be inserted into a stack as they are located in the page. Do not add things to the visited list until they are taken out of the stack.
    def dfs(self, source = "/wiki/Calvin_Li", goal = "/wiki/Wikipedia"):
        path = [source]

        # YOUR CODE HERE
        # ...
        path_exist = False
        queue = []
        seen = []
        queue.append(path)

        while queue:
            path = queue.pop()
            path_end = path[-1]

            if path_end not in seen:
                seen.append(path_end)
                html = self.internet.get_page(path_end)
                links = Parser().get_links_in_page(html)

                if goal in links:
                    path_exist = True
                    path.append(goal)
                    return path

                for link in links:
                    new_path = list(path)
                    new_path.append(link)
                    queue.append(new_path)

        if path_exist == False:
            return None # if no path exists, return None

class DijkstrasProblem:
    def __init__(self):
        self.internet = Internet()
    # Links should be inserted into the heap as they are located in the page.
    # By default, the cost of going to a link is the length of a particular destination link's name. For instance,
    #  if we consider /wiki/a -> /wiki/ab, then the default cost function will have a value of 8.
    # This cost function is overridable and your implementation will be tested on different cost functions. Use costFn(node1, node2)
    #  to get the cost of a particular edge.
    # You should return the path from source to goal that minimizes the total cost. Assume cost > 0 for all edges.
    def dijkstras(self, source = "/wiki/Calvin_Li", goal = "/wiki/Wikipedia", costFn = lambda x, y: len(y)):
        path = [source]

        # YOUR CODE HERE
        # ...
        path_exist = False
        queue = []
        seen = {}
        seen[source] = 0
        queue.append((0, path))

        while queue:
            pair = queue.pop(0)
            dist = pair[0]
            path = pair[1]
            path_end = path[-1]

            html = self.internet.get_page(path_end)
            links = Parser().get_links_in_page(html)
            
            if (goal in links) and (dist <= seen[path_end]):
                path_exist = True
                path.append(goal)
                return path

            for link in links:
                distance = costFn(path_end, link) + dist
                if (link not in seen) or (seen.get(link) > distance):
                    new_path = list(path)
                    new_path.append(link)
                    queue.append((distance, new_path))
                    seen[link] = distance
            queue.sort()

        if path_exist == False:
            return None # if no path exists, return None

class WikiracerProblem:
    def __init__(self):
        self.internet = Internet()

    # Time for you to have fun! Using what you know, try to efficiently find the shortest path between two wikipedia pages.
    # Your only goal here is to minimize the total amount of pages downloaded from the Internet, as that is the dominating time-consuming action.

    # Your answer doesn't have to be perfect by any means, but we want to see some creative ideas.
    # One possible starting place is to get the links in `goal`, and then search for any of those from the source page, hoping that those pages lead back to goal.

    # Note: a BFS implementation with no optimizations will not get credit, and it will suck.
    # You may find Internet.get_random() useful, or you may not.
    def self_define_parser(self, links):
        disallowed = ["(", ")"]

        # filter links using disallowed chars
        remove_links = []
        for i in range(len(links)):
            for char in disallowed:
                if links[i].find(char,6) != -1:
                    remove_links.append(links[i])
                    break

        # remove invalid links
        for link in remove_links:
            links.remove(link)

        return links

    def wikiracer(self, source = "/wiki/Calvin_Li", goal = "/wiki/Wikipedia"):

        source_path = [source]
        goal_path = [goal]
        possible_goal_path = [[goal]]

        # YOUR CODE HERE
        # ----- Double head BFS -----
        s_links = []
        g_links = []
        queue = []
        seen = []
        layer = 1
        path_exist = False

        queue.append(source_path)

        while queue:
            source_path = queue.pop(0)
            source_path_end = source_path[-1]
            goal_path_start = goal_path[0]
            
            if source_path_end not in self.internet.requests:
                s_html = self.internet.get_page(source_path_end)
                s_links = Parser().get_links_in_page(s_html)
                s_links = self.self_define_parser(s_links)

                # if goal is source, if find goal directly or find goal_path_start
                for path in possible_goal_path:
                    if path[0] in s_links:
                        source_path.extend(path)
                        return source_path

                if goal_path_start not in self.internet.requests:
                    g_html = self.internet.get_page(goal_path_start)
                    g_links = Parser().get_links_in_page(g_html)
                    g_links = self.self_define_parser(g_links)

                gather = list(set(s_links)&set(g_links))

                # find the connect path with 
                if len(gather) > 0:
                    for link in gather:
                        html = self.internet.get_page(link)
                        links = Parser().get_links_in_page(html)
                        if goal_path_start in links:
                            source_path.append(link)
                            source_path.extend(goal_path)
                            return source_path

                    for link in gather:
                        g_links.remove(link)

                    if len(queue) > 0:
                        if len(queue[0]) == layer + 1:
                            layer += 1
                            for link in g_links:
                                html = self.internet.get_page(link)
                                links = Parser().get_links_in_page(html)
                                if goal_path_start in links:
                                    goal_path.insert(0, link)
                                    new_path = list(goal_path)
                                    possible_goal_path.append(new_path)
                                    break

                for link in s_links:
                    if link not in seen:
                        new_path = list(source_path)
                        new_path.append(link)
                        queue.append(new_path)
                        seen.append(link)

        if path_exist == False:
            return None # if no path exists, return None

# KARMA
class FindInPageProblem:
    def __init__(self):
        self.internet = Internet()
    # This Karma problem is a little different. In this, we give you a source page, and then ask you to make up some heuristics that will allow you to efficiently
    #  find a page containing all of the words in `query`. Again, optimize for the fewest number of internet downloads, not for the shortest path.

    def find_in_page(self, source = "/wiki/Calvin_Li", query = ["ham", "cheese"]):

        raise NotImplementedError("Karma method find_in_page")

        path = [source]

        # find a path to a page that contains ALL of the words in query in any place within the page
        # path[-1] should be the page that fulfills the query.
        # YOUR CODE HERE

        return path # if no path exists, return None
