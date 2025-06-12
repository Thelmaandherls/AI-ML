CREATE (:ThreatActor {name: 'APT28', country: 'Russia'})
CREATE (:Vulnerability {cve: 'CVE-2024-1234', severity: 'High'})
CREATE (:Tool {name: 'Mimikatz'})
CREATE (:TTP {technique: 'Credential Dumping'})
// Create relationships
MATCH (a:ThreatActor), (t:Tool)
WHERE a.name = 'APT28' AND t.name = 'Mimikatz'
CREATE (a)-[:USES]->(t)
