select	p.payment_id
	,	p.payment_nm
from	payment	p
where	1=1
and		p.member_id = %(member_id)s
;