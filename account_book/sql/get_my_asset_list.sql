select	a.*
	,	c.id	as coin_id
from	(
			select	ma.asset_id
				,	ma.my_asset_id
				,	ma.my_asset_nm
				,	ma.ticker
				,	ma.price_div_cd
				,	ma.price
				,	ma.qty
				, 	a.asset_nm
				, 	ma.exchange_rate_yn
			from	my_asset	ma
				,	asset		a
			where	1=1
			and		ma.asset_id = a.asset_id
		) a
left outer join coin c
on		a.ticker = upper(c.symbol)
and		a.asset_id = '3'
where	1=1
;