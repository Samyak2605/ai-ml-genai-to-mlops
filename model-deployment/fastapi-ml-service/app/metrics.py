from prometheus_client import Counter

REQUEST_COUNT = Counter(
    "prediction_requests_total",
    "Total prediction requests"
)
