package com.security.mypage.dto;

import java.sql.Date;

import org.apache.ibatis.type.Alias;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
@Alias("MypageWorkBigThreeDto")
public class MypageWorkBigThreeDto {
	
	private String category;
	private int weight;
	private int counts;
	private Date endPostdate;

}
