import alpaca_trade_api
from app.brokerage.constants import PAPER_API_KEY, PAPER_END_POINT, PAPER_SECRET_KEY

def get_connection(real_money: bool = False) -> alpaca_trade_api.REST:
    """_summary_

    Args:
        real_money (bool, optional): _description_. Defaults to False.

    Returns:
        Any: _description_
    """
    if real_money:
        raise NotImplemented
    else:
        api = alpaca_trade_api.REST(
            key_id=PAPER_API_KEY,
            secret_key=PAPER_SECRET_KEY,
            base_url=PAPER_END_POINT,
        )
    return api