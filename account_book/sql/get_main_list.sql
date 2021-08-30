select	(ROW_NUMBER() OVER()) AS account_id
	,	zz.*
from	(
			select	z.account_id as seq
				,	z.account_dt
				,	z.division_nm
				,	z.member_nm
				,	z.payment_nm
				,	z.category_nm
				,	cd.category_seq_nm
				,	z.price
				,	z.remark
				,	z.impulse_yn
			from	(
						select	a.account_id
							,	a.account_dt
							,	d.division_nm
							,	am.member_nm
							,	p.payment_nm
							,	c.category_nm
							,	a.price
							,	a.remark
							,	a.impulse_yn
							,	a.category_id
							,	a.category_seq
						from	account			a
							,	division		d
							,	account_member	am
							,	payment			p
							,	category		c
						where	1=1
						and		a.division_id 	= d.division_id
						and		a.member_id   	= am.member_id
						and		a.payment_id  	= p.payment_id
						and		a.category_id 	= c.category_id
					) z
					left outer join category_dtl	cd
					on 		z.category_id 	= cd.category_id
					and		z.category_seq 	= cd.category_seq
			where	1=1
			order by z.account_dt
				,	 z.account_id
		) zz
where	1=1
;