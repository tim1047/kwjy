select	ma.accum_dt
	,	ma.asset_id
	,	a.asset_nm
	,	sum(ma.price * ma.qty) as total_sum_price
from	my_asset_accum	ma
	,	asset			a
where	1=1
and		ma.asset_id = a.asset_id
and		ma.accum_dt = %(proc_dt)s
group by ma.accum_dt, ma.asset_id, a.asset_nm
