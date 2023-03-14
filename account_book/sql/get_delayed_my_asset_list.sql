select	a.*
	,	mg.my_asset_group_nm
from	(
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
				,	ma.my_asset_group_id
				,   maa.mod_dts							as my_asset_accum_dts
			from	my_asset		ma
				,	my_asset_accum 	maa
				,	asset			a
			where	1=1
			and		ma.my_asset_id 	= maa.my_asset_id
			and		ma.asset_id 	= a.asset_id
			and		maa.accum_dt 	= %(proc_dt)s
		) a
left outer join my_asset_group mg
on 	a.my_asset_group_id = mg.my_asset_group_id
;