update  account
set     account_dt      = coalesce(nullif(%(account_dt)s, ''), account_dt)
    ,   division_id     = coalesce(nullif(%(division_id)s, ''), division_id)
    ,   member_id       = coalesce(nullif(%(member_id)s, ''), member_id)
    ,   payment_id      = coalesce(nullif(%(payment_id)s, ''), payment_id)
    ,   category_id     = coalesce(nullif(%(category_id)s, ''), category_id)
    ,   category_seq    = coalesce(nullif(%(category_seq)s, ''), category_seq)
    ,   price           = coalesce(nullif(%(price)s, 0), price)
    ,   remark          = %(remark)s
    ,   impulse_yn      = coalesce(nullif(%(impulse_yn)s, ''), impulse_yn)
    ,   point_yn        = coalesce(nullif(%(point_yn)s, ''), point_yn)
    ,   mod_dts         = now()
where   1=1
and     account_id = %(account_id)s
;