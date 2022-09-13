insert into account (
	account_id
  , account_dt
  , division_id
  , member_id
  , payment_id
  , category_id
  , category_seq
  , price
  , remark
  , impulse_yn
  , point_price
  , reg_dts
  ,	regpe_id
  , mod_dts
  , modpe_id
)
values
(
	  nextval('seq_account')
  , %(account_dt)s
  , %(division_id)s
  , %(member_id)s
  , %(payment_id)s
  , %(category_id)s
  , %(category_seq)s
  , %(price)s
  , %(remark)s
  , %(impulse_yn)s
  , %(point_price)s
  ,	now()
  , 'SKW'
  , now()
  , 'SKW'
)
;