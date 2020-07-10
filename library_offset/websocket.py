from lib_web.models import Book
from django.apps import apps
from syncasync import sync_to_async

@sync_to_async
def get_amount(books):
	return books.objects.all().count()


async def websocket_application(scope, receive, send):
	
	while True:
		Book = apps.get_model('lib_web', 'Book')
		event = await receive()
		
		if event['type'] == 'websocket.connect':
			await send({'type': 'websocket.accept'})
		
		if event['type'] == 'websocket.disconnect':
			break
			
		if event['type'] == 'websocket.receive':
			if event['text'] == 'storage_state':
				amount_books = await get_amount(Book)
				await send({
					'type': 'websocket.send',
					'text': str(amount_books)
				})
