import aiohttp

class DBWriter:
    def __init__(self, username="johnson.newbie@world.com", password="johnson.newbie@world.com"):
        self.username = username
        self.password = password
        self.token = None
        pass
 
    async def getToken(self):
        # keyurl = "http://host.docker.internal:33001/oauth/login3"
        if self.token:
            return self.token
       
        keyurl = "http://localhost:33001/oauth/login3"
        async with aiohttp.ClientSession() as session:
            async with session.get(keyurl) as resp:
                # print(resp.status)
                keyJson = await resp.json()
                # print(keyJson)
 
            payload = {"key": keyJson["key"], "username": self.username, "password": self.password}
            async with session.post(keyurl, json=payload) as resp:
                # print(resp.status)
                tokenJson = await resp.json()
                # print(tokenJson)
        self.token = tokenJson.get("token", None)
        return self.token
 
    async def queryGQL(self, query, variables=False):
        # gqlurl = "http://host.docker.internal:33001/api/gql"
        gqlurl = "http://localhost:33001/api/gql"
        token = self.token
        if token is None:
            token = await self.getToken()
        if variables:
            payload = {"query": query, "variables": variables}
        else:
            payload = {"query": query}
        # headers = {"Authorization": f"Bearer {token}"}
        cookies = {'authorization': token}
        async with aiohttp.ClientSession() as session:
            # print(headers, cookies)
            async with session.post(gqlurl, json=payload, cookies=cookies) as resp:
                # print(resp.status)
                if resp.status != 200:
                    text = await resp.text()
                    print(f"failed query \n{query}\n with variables {variables}".replace("'", '"'))
                    print(f"failed resp.status={resp.status}, text={text}")
                    raise Exception(f"Unexpected GQL response", text)
                else:
                    response = await resp.json()
                    return response  