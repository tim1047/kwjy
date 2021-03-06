select	ma.asset_id
	,	ma.my_asset_id
	,	ma.my_asset_nm
	,	ma.ticker
	,	ma.price
	,	ma.qty
	, 	a.asset_nm
	,	ma.ticker
	,	ma.price_div_cd
	,	ma.exchange_rate_yn
	,	cast(maa.price * maa.qty as integer) as sum_price
from	my_asset		ma
	,	my_asset_accum 	maa
	,	asset			a
where	1=1
and		ma.my_asset_id 	= maa.my_asset_id
and		ma.asset_id 	= a.asset_id
and		maa.accum_dt 	= %(proc_dt)s