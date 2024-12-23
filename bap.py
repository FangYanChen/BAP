from collections import defaultdict, deque

def find_connected_components(edges):
      graph = defaultdict(list)
      for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

      visited = set()
      components = []

      def bfs(node):
            queue = deque([node])
            component = []
            visited.add(node)

            while queue:
                  current = queue.popleft()
                  component.append(current)
                  for neighbor in graph[current]:
                        if neighbor not in visited:
                              visited.add(neighbor)
                              queue.append(neighbor)
            return component

      for user in graph:
            if user not in visited:
                  components.append(bfs(user))

      return components

def recommend_new_friends(components, edges):
      existing_connections = set(edges)

      user_to_component = {}
      for component_id, component in enumerate(components):
            for user in component:
                  user_to_component[user] = component_id

      recommendations = defaultdict(list)

      for user, component_id in user_to_component.items():
            potential_friends = [
                  potential_friend
                  for other_component_id, component in enumerate(components)
                  if other_component_id != component_id
                  for potential_friend in component
            ]

            for potential_friend in potential_friends:
                  if (user, potential_friend) not in existing_connections and (
                  potential_friend, user
                  ) not in existing_connections:
                        recommendations[user].append(potential_friend)

      return recommendations

edges = [
      ("Alice", "Bob"),
      ("Bob", "Charlie"),
      ("David", "Eve"),
      ("Eve", "Frank"),
      ("Grace", "Hannah"),
      ("Grace", "Ivy"),
]

components = find_connected_components(edges)
print("find_connected_components:")
for idx, component in enumerate(components):
      print(f"component {idx + 1}: {component}")

recommendations = recommend_new_friends(components, edges)
print("\nrecommend_new_friends:")
for user, friends in recommendations.items():
      print(f"{user}: {friends}")
