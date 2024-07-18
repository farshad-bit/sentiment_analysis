import fetchMock from 'jest-fetch-mock';
import { analyzeAdvancedSentiment } from '../../src/views/static/js/advanced_sentiment';

fetchMock.enableMocks();

global.alert = jest.fn();

beforeEach(() => {
  fetch.resetMocks();
  global.alert.mockClear();
});

test('analyzeAdvancedSentiment success', async () => {
  fetch.mockResponseOnce(JSON.stringify({ sentiment: 'positive' }), { status: 200 });

  await analyzeAdvancedSentiment();

  expect(fetch).toHaveBeenCalledWith('/api/advanced_sentiment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer test_token',
      'X-CSRF-TOKEN': 'test_csrf_token'
    },
    body: JSON.stringify({ text: 'Some text' })
  });
});

test('analyzeAdvancedSentiment unauthorized', async () => {
  fetch.mockResponseOnce(JSON.stringify({ message: 'Unauthorized' }), { status: 401 });

  await analyzeAdvancedSentiment();

  expect(alert).toHaveBeenCalledWith('Unauthorized. Please log in again.');
});

test('analyzeAdvancedSentiment failure', async () => {
  fetch.mockRejectOnce(new Error('API is down'));

  await analyzeAdvancedSentiment();

  expect(alert).toHaveBeenCalledWith('Advanced sentiment analysis failed');
});
