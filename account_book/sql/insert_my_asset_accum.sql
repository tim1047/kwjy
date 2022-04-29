insert into my_asset_accum
(
	accum_dt
  , my_asset_id
  , my_asset_nm
  , asset_id
  , ticker
  ,	price
  ,	qty
  , reg_dts
  ,	regpe_id
  ,	mod_dts
  ,	modpe_id
)
values
(
  %(accum_dt)s
  , %(my_asset_id)s
  , %(my_asset_nm)s
  , %(asset_id)s
  , %(ticker)s
  , %(price)s
  , %(qty)s
  , now()
  , 'SKW'
  , now()
  , 'SKW'
)
on conflict (accum_dt, my_asset_id) do
update
set   price = %(price)s, qty = %(qty)s, mod_dts = now()
;