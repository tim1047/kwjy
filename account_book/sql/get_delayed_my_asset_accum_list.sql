select	ma.asset_id
	,	ma.my_asset_id
	,	ma.my_asset_nm
	,	ma.ticker
	,	ma.price
	,	ma.qty
	, 	a.asset_nm
	,	cast(ma.price * ma.qty as integer) as sum_price
from	my_asset_accum 	ma
	,	asset			a
where	1=1
and		ma.asset_id = a.asset_id
and		ma.accum_dt = %(proc_dt)s
;