from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.execute_query(query, parameters)

    def create_match(self):
        query = "CREATE (:Match)"
        self.execute_query(query)
        
        def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.execute_query(query, parameters)

    def create_match(self):
        query = "CREATE (:Match)"
        self.execute_query(query)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self, match_id):
        query = "MATCH (m:Match) WHERE id(m) = $match_id RETURN id(m) AS match_id"
        parameters = {"match_id": match_id}
        result = self.execute_query(query, parameters)
        return result[0]["match_id"] if result else None
        def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.execute_query(query, parameters)

    def create_match(self):
        query = "CREATE (:Match)"
        self.execute_query(query)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self, match_id):
        query = "MATCH (m:Match) WHERE id(m) = $match_id RETURN id(m) AS match_id"
        parameters = {"match_id": match_id}
        result = self.execute_query(query, parameters)
        return result[0]["match_id"] if result else None

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.execute_query(query, parameters)

    def get_player_matches(self, player_name):
        query = "MATCH (:Player {name: $player_name})-[:PARTICIPATES_IN]->(m:Match) RETURN id(m) AS match_id"
        parameters = {"player_name": player_name}
        results = self.execute_query(query, parameters)
        return [result["match_id"] for result in results]

    def record_match_result(self, match_id, results):
        for player_name, score in results.items():
            query = """
                MATCH (p:Player {name: $player_name})
                MATCH (m:Match) WHERE id(m) = $match_id
                CREATE (p)-[:PARTICIPATES_IN {score: $score}]->(m)
            """
            parameters = {"player_name": player_name, "match_id": match_id, "score": score}
            self.execute_query(query, parameters)    
