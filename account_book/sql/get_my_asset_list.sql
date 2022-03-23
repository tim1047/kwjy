select	ma.asset_id
	,	ma.my_asset_id
	,	ma.my_asset_nm
	,	ma.ticker
	,	ma.price_div_cd
	,	ma.price
	,	ma.qty
	, 	a.asset_nm
from	my_asset	ma
	,	asset		a
where	1=1
and		ma.asset_id = a.asset_id
;