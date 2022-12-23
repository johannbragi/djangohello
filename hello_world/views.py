from django.shortcuts import render
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def hello_world(request):
    logger.error("Some loggin")
    return render(request, "hello_world.html", {})
