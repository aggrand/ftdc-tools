from typing import List
from unittest.mock import MagicMock

from ftdc_tools.decode import FTDCDoc
from ftdc_tools.rollups.client_perf import ClientPerformanceStatistics, Statistic

req_get = MagicMock()
req_get.raw = []


def test_ftdc_statistic(mock_ftdc_stream_output: List[FTDCDoc]) -> None:
    expected_response = [
        Statistic(
            name="AverageLatency",
            value=415.6,
            version=3,
            user_submitted=False,
        ),
        Statistic(name="AverageSize", value=1.8, version=3, user_submitted=False),
        Statistic(
            name="OperationThroughput",
            value=1111.0809711108097,
            version=5,
            user_submitted=False,
        ),
        Statistic(
            name="DocumentThroughput",
            value=1111.0809711108097,
            version=1,
            user_submitted=False,
        ),
        Statistic(name="ErrorRate", value=0.0, version=5, user_submitted=False),
        Statistic(
            name="SizeThroughput",
            value=1999.9457479994574,
            version=5,
            user_submitted=False,
        ),
        Statistic(name="WorkersMin", value=0, version=3, user_submitted=False),
        Statistic(name="WorkersMax", value=0, version=3, user_submitted=False),
        Statistic(name="LatencyMin", value=299.0, version=4, user_submitted=False),
        Statistic(
            name="LatencyMax",
            value=881.0,
            version=4,
            user_submitted=False,
        ),
        Statistic(
            name="DurationTotal",
            value=9000244.140625,
            version=5,
            user_submitted=False,
        ),
        Statistic(name="ErrorsTotal", value=0, version=3, user_submitted=False),
        Statistic(name="OperationsTotal", value=10, version=3, user_submitted=False),
        Statistic(name="DocumentsTotal", value=10, version=0, user_submitted=False),
        Statistic(name="SizeTotal", value=18, version=3, user_submitted=False),
        Statistic(
            name="OverheadTotal",
            value=180009973872,
            version=1,
            user_submitted=False,
        ),
        Statistic(
            name="Latency50thPercentile",
            value=377.0,
            version=4,
            user_submitted=False,
        ),
        Statistic(
            name="Latency80thPercentile",
            value=412.4,
            version=4,
            user_submitted=False,
        ),
        Statistic(
            name="Latency90thPercentile",
            value=712.6999999999998,
            version=4,
            user_submitted=False,
        ),
        Statistic(
            name="Latency95thPercentile",
            value=881.0,
            version=4,
            user_submitted=False,
        ),
        Statistic(
            name="Latency99thPercentile",
            value=881.0,
            version=4,
            user_submitted=False,
        ),
    ]

    roll = ClientPerformanceStatistics()
    for doc in mock_ftdc_stream_output:
        roll.add_doc(doc)
    all_statistics = roll.all_statistics
    assert all_statistics == expected_response


# @patch("ftdc_tools.decoder.FTDC.__iter__")
# def test_empty_ftdc_statistic(self, mock_ftdc_decoder) -> None:
#    mock_ftdc_decoder.return_value = iter([])
#    expected_response = [
#        Statistic(
#            name="AverageLatency",
#            value=0,
#            version=3,
#            user_submitted=False,
#        ),
#        Statistic(name="AverageSize", value=0, version=3, user_submitted=False),
#        Statistic(
#            name="OperationThroughput",
#            value=0,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="DocumentThroughput",
#            value=0,
#            version=1,
#            user_submitted=False,
#        ),
#        Statistic(name="ErrorRate", value=0, version=5, user_submitted=False),
#        Statistic(
#            name="SizeThroughput",
#            value=0.0,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(name="WorkersMin", value=0, version=3, user_submitted=False),
#        Statistic(name="WorkersMax", value=0, version=3, user_submitted=False),
#        Statistic(
#            name="LatencyMin",
#            value=0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(name="LatencyMax", value=0, version=4, user_submitted=False),
#        Statistic(
#            name="DurationTotal",
#            value=0.0,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(name="ErrorsTotal", value=0, version=3, user_submitted=False),
#        Statistic(name="OperationsTotal", value=0, version=3, user_submitted=False),
#        Statistic(name="DocumentsTotal", value=0, version=0, user_submitted=False),
#        Statistic(name="SizeTotal", value=0, version=3, user_submitted=False),
#        Statistic(
#            name="OverheadTotal",
#            value=0,
#            version=1,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency50thPercentile",
#            value=0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency80thPercentile",
#            value=0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency90thPercentile",
#            value=0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency95thPercentile",
#            value=0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency99thPercentile",
#            value=0,
#            version=4,
#            user_submitted=False,
#        ),
#    ]
#    stats = GennyClientEventsFTDCStatistics(b"dummy_string")
#    all_statistics = stats.all_statistics
#
#    assert all_statistics == expected_response
#
# @patch("ftdc_tools.decoder.FTDC.__iter__")
# def test_single_ftdc_statistic(self, mock_ftdc_decoder) -> None:
#    mock_ftdc_decoder.return_value = iter(
#        [
#            {
#                "ts": 1643735930767,
#                "id": 0,
#                "counters" {
#                    "n": 1,
#                    "ops": 1,
#                    "size": 0,
#                    "errors": 0,
#                },
#                "timers": {
#                    "dur": 366,
#                    "total": 180009841025
#                },
#                "gauges": {
#                    "state": 0,
#                    "workers": 1,
#                    "failed": 0
#                }
#            }
#        ]
#    )
#    expected_response = [
#        Statistic(
#            name="AverageLatency",
#            value=366.0,
#            version=3,
#            user_submitted=False,
#        ),
#        Statistic(name="AverageSize", value=0.0, version=3, user_submitted=False),
#        Statistic(
#            name="OperationThroughput",
#            value=4096000.0,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="DocumentThroughput",
#            value=4096000.0,
#            version=1,
#            user_submitted=False,
#        ),
#        Statistic(name="ErrorRate", value=0.0, version=5, user_submitted=False),
#        Statistic(
#            name="SizeThroughput",
#            value=0.0,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(name="WorkersMin", value=0, version=3, user_submitted=False),
#        Statistic(name="WorkersMax", value=0, version=3, user_submitted=False),
#        Statistic(
#            name="LatencyMin",
#            value=366.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(name="LatencyMax", value=366.0, version=4, user_submitted=False),
#        Statistic(
#            name="DurationTotal",
#            value=244.140625,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(name="ErrorsTotal", value=0, version=3, user_submitted=False),
#        Statistic(name="OperationsTotal", value=1, version=3, user_submitted=False),
#        Statistic(name="DocumentsTotal", value=1, version=0, user_submitted=False),
#        Statistic(name="SizeTotal", value=0, version=3, user_submitted=False),
#        Statistic(
#            name="OverheadTotal",
#            value=180009840659,
#            version=1,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency50thPercentile",
#            value=366.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency80thPercentile",
#            value=366.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency90thPercentile",
#            value=366.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency95thPercentile",
#            value=366.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency99thPercentile",
#            value=366.0,
#            version=4,
#            user_submitted=False,
#        ),
#    ]
#
#    stats = GennyClientEventsFTDCStatistics(b"dummy_ftdc_data")
#    all_statistics = stats.all_statistics
#
#    assert all_statistics == expected_response
#
# @patch("ftdc_tools.decoder.FTDC.__iter__")
# def test_invalid_ftdc_record(self, mock_ftdc_decoder) -> None:
#    mock_ftdc_decoder.return_value = iter(
#        [
#            {
#                "ts": 1643735930767,
#                "id": 0,
#                "counters" {
#                    "n": 1,
#                    "ops": 1,
#                    "size": 0,
#                    "errors": 0,
#                },
#                "timers": {
#                    "total": 180009841025
#                },
#                "gauges": {
#                    "state": 0,
#                    "workers": 1,
#                    "failed": 0
#                }
#            }
#        ]
#    )
#    with pytest.raises(ValueError) as exc_info:
#        GennyClientEventsFTDCStatistics(b"dummy_ftdc_data")._process()
#
#    assert (
#        str(exc_info.value)
#        == "Missing field - (b'timers', b'duration') - duration in Genny client side FTDC record."
#    )
#
# @patch("ftdc_tools.decoder.FTDC.__iter__")
# def test_non_linear_ftdc_statistic(
#    self, mock_ftdc_decoder, mock_non_linear_ftdc_stream_output
# ) -> None:
#    mock_ftdc_decoder.return_value = iter(mock_non_linear_ftdc_stream_output)
#
#    expected_response = [
#        Statistic(
#            name="AverageLatency",
#            value=4156111.1,
#            version=3,
#            user_submitted=False,
#        ),
#        Statistic(name="AverageSize", value=1.8, version=3, user_submitted=False),
#        Statistic(
#            name="OperationThroughput",
#            value=632.5087247907595,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="DocumentThroughput",
#            value=632.5087247907595,
#            version=1,
#            user_submitted=False,
#        ),
#        Statistic(name="ErrorRate", value=0.0, version=5, user_submitted=False),
#        Statistic(
#            name="SizeThroughput",
#            value=1138.5157046233671,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(name="WorkersMin", value=0, version=3, user_submitted=False),
#        Statistic(name="WorkersMax", value=0, version=3, user_submitted=False),
#        Statistic(name="LatencyMin", value=366111.0, version=4, user_submitted=False),
#        Statistic(
#            name="LatencyMax",
#            value=8810000.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="DurationTotal",
#            value=15810058.593749998,
#            version=5,
#            user_submitted=False,
#        ),
#        Statistic(name="ErrorsTotal", value=0, version=3, user_submitted=False),
#        Statistic(name="OperationsTotal", value=10, version=3, user_submitted=False),
#        Statistic(name="DocumentsTotal", value=10, version=0, user_submitted=False),
#        Statistic(name="SizeTotal", value=18, version=3, user_submitted=False),
#        Statistic(
#            name="OverheadTotal",
#            value=179968416917,
#            version=1,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency50thPercentile",
#            value=3920000.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency80thPercentile",
#            value=5800999.999999999,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency90thPercentile",
#            value=8093166.666666666,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency95thPercentile",
#            value=8810000.0,
#            version=4,
#            user_submitted=False,
#        ),
#        Statistic(
#            name="Latency99thPercentile",
#            value=8810000.0,
#            version=4,
#            user_submitted=False,
#        ),
#    ]
#    roll = GennyClientEventsFTDCStatistics(b"dummy_string")
#    all_statistics = roll.all_statistics
#
#    assert all_statistics == expected_response
