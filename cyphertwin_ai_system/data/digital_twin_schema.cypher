CREATE (:Asset {id: 'srv01', os: 'Windows', patchLevel: 'low'}),
       (:Asset {id: 'srv02', os: 'Linux', patchLevel: 'high'}),
       (:User {username: 'admin', role: 'superuser'}),
       (:Service {name: 'RDP', status: 'running'}),
       (:Finding {type: 'UnpatchedSoftware', severity: 'high'});

MATCH (a:Asset {id: 'srv01'}), (f:Finding {type: 'UnpatchedSoftware'})
CREATE (a)-[:HAS_FINDING]->(f);
