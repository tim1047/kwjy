select	a.account_id
	,	a.account_dt
	,	d.division_nm
	,	am.member_nm
	,	p.payment_nm
	,	c.category_nm
	,	cd.category_seq_nm
	,	a.price
	,	a.remark
	,	a.impluse_yn
from	account			a
	,	division		d
	,	account_member	am
	,	payment			p
	,	category		c
	,	category_dtl	cd
where	1=1
and		a.division_id 	= d.division_id
and		a.member_id   	= am.member_id
and		a.payment_id  	= p.payment_id
and		a.category_id 	= c.category_id
and		a.category_id 	= cd.category_id
and		a.category_seq 	= cd.category_seq
order by a.account_id
;