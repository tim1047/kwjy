update  account
set     account_dt      = coalesce(nullif(%(account_dt)s, ''), account_dt)
    ,   division_id     = coalesce(nullif(%(division_id)s, ''), division_id)
    ,   member_id       = coalesce(nullif(%(member_id)s, ''), member_id)
    ,   payment_id      = coalesce(nullif(%(payment_id)s, ''), payment_id)
    ,   category_id     = coalesce(nullif(%(category_id)s, ''), category_id)
    ,   category_seq    = coalesce(nullif(%(category_seq)s, ''), category_seq)
    ,   price           = coalesce(nullif(%(price)s, ''), price)
    ,   remark          = coalesce(nullif(%(remark)s, ''), remark)
    ,   impulse_yn      = coalesce(nullif(%(impulse_yn)s, ''), impulse_yn)
    ,   mod_dts         = now()
where   1=1
and     account_id = %(account_id)s
;