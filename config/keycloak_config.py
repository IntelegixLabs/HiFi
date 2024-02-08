from schemas import *


settings = authConfiguration(
    server_url="http://localhost:8080/",
    realm="GlobeHopper",
    client_id="globehopper",
    client_secret="uYVPTRHKDWtKmCy1yWmotAoXfvaqkyvO",
    authorization_url="http://localhost:8080/realms/GlobeHopper/protocol/openid-connect/auth",
    token_url="http://localhost:8080/realms/GlobeHopper/protocol/openid-connect/token",
)