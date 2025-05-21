import asyncio
import pytest
from fetch_data import fetch_data

@pytest.mark.asyncio
async def test_fetch_data():
    # Call the async function
    result = await fetch_data()
    
    # Check if the result is as expected
    assert result == {'data': 'some data'}