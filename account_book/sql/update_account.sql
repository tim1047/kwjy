update  account
set     account_dt      = coalesce(%(account_dt)s, account_dt)
    ,   division_id     = coalesce(%(division_id)s, division_id)
    ,   member_id       = coalesce(%(member_id)s, member_id)
    ,   payment_id      = coalesce(%(payment_id)s, payment_id)
    ,   category_id     = coalesce(%(category_id)s, category_id)
    ,   category_seq    = coalesce(%(category_seq)s, category_seq)
    ,   price           = coalesce(%(price)s, price)
    ,   remark          = coalesce(%(remark)s, remark)
    ,   impulse_yn      = coalesce(%(impulse_yn)s, impulse_yn)
    ,   mod_dts         = now()
where   1=1
and     account_id = %(account_id)s
;