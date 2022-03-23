update  my_asset
set     my_asset_nm     	= coalesce(nullif(%(my_asset_nm)s, ''), my_asset_nm)
    ,   asset_id     		= coalesce(nullif(%(asset_id)s, ''), asset_id)
    ,   ticker       		= coalesce(nullif(%(ticker)s, ''), ticker)
    ,   price_div_cd    	= coalesce(nullif(%(price_div_cd)s, ''), price_div_cd)
    ,   price           	= coalesce(nullif(%(price)s, 0), price)
    ,   qty          		= coalesce(nullif(%(qty)s, 0.0), qty)
    ,   exchange_rate_yn 	= coalesce(nullif(%(exchange_rate_yn)s, ''), exchange_rate_yn)
    ,   mod_dts         	= now()
where   1=1
and     my_asset_id = %(my_asset_id)s
;