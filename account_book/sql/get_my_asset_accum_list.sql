select	b.accum_dt
	,	a.asset_id
	,	a.asset_nm
	,	coalesce(b.total_sum_price, 0) as total_sum_price
from	asset	a
left outer join
		(
			select	ma.accum_dt
				,	ma.asset_id
				,	a.asset_nm
				,	sum(ma.price * ma.qty) as total_sum_price
			from	asset	a
				,	my_asset_accum	ma
			where	1=1
			and		a.asset_id = ma.asset_id
			and		ma.accum_dt = %(proc_dt)s
			group by ma.accum_dt, ma.asset_id, a.asset_nm
		) b
on		a.asset_id = b.asset_id
where	1=1
order by a.asset_id