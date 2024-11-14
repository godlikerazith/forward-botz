from aiohttp import web

routes = web.RouteTableDef()

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Silicon")

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
    
# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay
