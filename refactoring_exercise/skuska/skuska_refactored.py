from typing import List, Set, Tuple, Dict


class Garden:

    def __init__(self, file_name: str) -> None:
        self.garden: Dict[str: Dict[str]] = {}
        self.file_name: str = file_name
        self.fruits: Set[str] = set()
        self.solution: List[str] = []
        self._create_graph(self._read_file())

    def _read_file(self) -> List[List[str]]:
        with open(self.file_name, 'r') as file:
            return [row.split() for row in file.read().splitlines()]

    def _add_edge(self, vertex1: str, vertex2: str, fruit: str) -> None:
        if self._vertex_exists(vertex1):
            self.garden[vertex1][vertex2] = fruit
        else:
            self.garden[vertex1] = {vertex2: fruit}

    def _vertex_exists(self, vertex: str) -> bool:
        return vertex in self.garden

    def _create_graph(self, rows: List[List[str]]) -> None:
        for row in rows:
            if self._row_contains_fruit(row):
                vertex1, fruit, vertex2 = row[0], row[1], row[2]
                self.fruits.add(fruit)
            else:
                vertex1, fruit, vertex2 = row[0], '', row[1]
            self._add_edge(vertex1, vertex2, fruit)
            self._add_edge(vertex2, vertex1, fruit)

    @staticmethod
    def _row_contains_fruit(row: List[str]) -> bool:
        if len(row) == 3:
            return True
        elif len(row) == 2:
            return False
        raise RuntimeError("Row has incorrect number of items")

    def vertices(self) -> Set[str]:
        return set(self.garden.keys())

    def edge(self, v1: str, v2: str) -> str:
        try:
            return self.garden[v1][v2]
        except KeyError:
            return None

    def fruit_types(self) -> Set[str]:
        return self.fruits

    def backtracking(self, start_vertex: str, visited_edges: Set[Tuple[str]],
                     path: List[str], collected_fruits: Set[str]) -> None:
        if collected_fruits >= self.fruit_types():
            self.solution = path
        else:
            for adjacent_vertex in self.garden[start_vertex]:
                if self._can_continue(start_vertex, adjacent_vertex, visited_edges, collected_fruits):
                    new_visited_edges = visited_edges.union({(start_vertex, adjacent_vertex),
                                                                              (adjacent_vertex, start_vertex)})
                    new_path = path + [adjacent_vertex]
                    new_collected_fruits = collected_fruits.union(self.edge(adjacent_vertex, start_vertex))
                    self.backtracking(adjacent_vertex, new_visited_edges, new_path, new_collected_fruits)

    def _can_continue(self, start_vertex: str, end_vertex: str,
                      visited_edges: Set[Tuple[str]], collected_fruits: Set[str]) -> bool:
        if (start_vertex, end_vertex) in visited_edges or self.edge(start_vertex, end_vertex) in collected_fruits \
                or self.solution:
            return False
        return True

    def start(self, start_vertex: str) -> List[str]:
        self.solution.clear()
        self.backtracking(start_vertex, set(), [start_vertex], set())
        return self.solution


if __name__ == '__main__':
    g = Garden('subor1.txt')
    for v1, v2 in ('3', '2'), ('2', '3'), ('5', '4'), ('2', '6'), ('5', '1'):
        print(f'edge({v1!r}, {v2!r}) = {g.edge(v1, v2)!r}')
    print('fruit types =', g.fruit_types())
    for v1 in sorted(g.vertices()):
        print(f'path from {v1!r}:', g.start(v1))
