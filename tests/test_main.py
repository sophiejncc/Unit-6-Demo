# Arrange
# Act
# Assert

from helpers.file_helpers import read_csv


def test_read_csv():
    # Arrange - define the input for the test
    filename = "data/stock_data.csv"
    # Act - this is the function we want to test (the function will be called read_csv)
    data = read_csv(filename)
    # Assert - this is the output we expect, i.e. there is some data there
    assert len(data) > 0
