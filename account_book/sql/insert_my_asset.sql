insert into my_asset
(
	my_asset_id
  , my_asset_nm
  , asset_id
  ,	ticker
  ,	price_div_cd
  ,	price
  ,	qty
  ,	exchange_rate_yn
  , reg_dts
  ,	regpe_id
  ,	mod_dts
  ,	modpe_id
)
values
(
	nextval('seq_my_asset')
  , %(my_asset_nm)s
  , %(asset_id)s
  , %(ticker)s
  , %(price_div_cd)s
  , %(price)s
  , %(qty)s
  , %(exchange_rate_yn)s
  , now()
  , 'SKW'
  , now()
  , 'SKW'
)
;