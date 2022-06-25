select	c.category_id
	,	c.category_seq
	,	c.category_seq_nm
from	category_dtl	c
where	1=1
and		c.category_id = %(category_id)s
order by c.category_id, c.category_seq
;