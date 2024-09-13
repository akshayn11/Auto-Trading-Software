# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
from datetime import datetime,date,timedelta
import time
import threading
import logging

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 812,470 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"                                             				 Auto Trading  Software", wx.DefaultPosition, wx.Size( 700,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 14, 72, 90, 90, False, "Cambria" ) )
		
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( fgSizer2, 0, wx.EXPAND, 5 )
		
		fgSizer9 = wx.FlexGridSizer( 3, 6, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		self.m_staticText38.Wrap( -1 )
		fgSizer9.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		index_boxChoices = [ u"NIFTY", u"BANKNIFTY", u"FINNIFTY", u"MIDCPNIFTY", u"SENSEX", u"BANKEX" ]
		self.index_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), index_boxChoices, 0 )
		self.index_box.SetSelection( 0 )
		fgSizer9.Add( self.index_box, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText39.Wrap( -1 )
		fgSizer9.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		expiry_boxChoices = []
		self.expiry_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), expiry_boxChoices, 0 )
		self.expiry_box.SetSelection( 0 )
		fgSizer9.Add( self.expiry_box, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText40.Wrap( -1 )
		fgSizer9.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		product_boxChoices = [ u"MIS", u"NRML" ]
		self.product_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), product_boxChoices, 0 )
		self.product_box.SetSelection( 0 )
		fgSizer9.Add( self.product_box, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer9.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer9.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer9.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.time_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		fgSizer9.Add( self.time_box, 0, wx.ALL, 5 )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText45.Wrap( -1 )
		fgSizer9.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		timeframe_boxChoices = [ u"1",u"2",u"5", u"10" ]
		self.timeframe_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), timeframe_boxChoices, 0 )
		self.timeframe_box.SetSelection( 0 )
		fgSizer9.Add( self.timeframe_box, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( fgSizer9, 0, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"High & Low" ), wx.VERTICAL )
		
		
		bSizer2.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		gSizer14 = wx.GridSizer( 0, 8, 0, 0 )
		
		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u" CE-LOW", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText75.Wrap( -1 )
		gSizer14.Add( self.m_staticText75, 0, wx.ALL, 5 )
		
		self.ce_low = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ce_low.Wrap( -1 )
		gSizer14.Add( self.ce_low, 0, wx.ALL, 5 )
		
		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, u"CE-HIGH", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText77.Wrap( -1 )
		gSizer14.Add( self.m_staticText77, 0, wx.ALL, 5 )
		
		self.ce_high = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ce_high.Wrap( -1 )
		gSizer14.Add( self.ce_high, 0, wx.ALL, 5 )
		
		self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u" PE-LOW", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText83.Wrap( -1 )
		gSizer14.Add( self.m_staticText83, 0, wx.ALL, 5 )
		
		self.pe_low = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.pe_low.Wrap( -1 )
		gSizer14.Add( self.pe_low, 0, wx.ALL, 5 )
		
		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u" PE-HIGH", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		gSizer14.Add( self.m_staticText85, 0, wx.ALL, 5 )
		
		self.pe_high = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.pe_high.Wrap( -1 )
		gSizer14.Add( self.pe_high, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer14, 0, wx.EXPAND, 0 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"INPUT" ), wx.VERTICAL )
		
		fgSizer11 = wx.FlexGridSizer( 6, 6, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText46 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer11.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"   Strike", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText47.Wrap( -1 )
		fgSizer11.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"      Quantity", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText48.Wrap( -1 )
		fgSizer11.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"         SL", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText49.Wrap( -1 )
		fgSizer11.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"      Target", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer11.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"   Status bar", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer11.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"        CE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		fgSizer11.Add( self.m_staticText52, 0, wx.ALL, 5 )
		
		self.ce_strike = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.ce_strike, 0, wx.ALL, 5 )
		
		self.ce_qty = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.ce_qty, 0, wx.ALL, 5 )
		
		self.ce_sl = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.ce_sl, 0, wx.ALL, 5 )
		
		self.ce_target = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.ce_target, 0, wx.ALL, 5 )
		
		self.ce_status = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.ce_status, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer11.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.ce_ltp_ = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ce_ltp_.Wrap( -1 )
		fgSizer11.Add( self.ce_ltp_, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText27.Wrap( -1 )
		fgSizer11.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer11.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText29.Wrap( -1 )
		fgSizer11.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer11.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.m_staticText55 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"        PE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		fgSizer11.Add( self.m_staticText55, 0, wx.ALL, 5 )
		
		self.pe_strike = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.pe_strike, 0, wx.ALL, 5 )
		
		self.pe_qty = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.pe_qty, 0, wx.ALL, 5 )
		
		self.pe_sl = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.pe_sl, 0, wx.ALL, 5 )
		
		self.pe_target = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.pe_target, 0, wx.ALL, 5 )
		
		self.pe_status = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.pe_status, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText32.Wrap( -1 )
		fgSizer11.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.pe_ltp_ = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.pe_ltp_.Wrap( -1 )
		fgSizer11.Add( self.pe_ltp_, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer11.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer11.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer11.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText37.Wrap( -1 )
		fgSizer11.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer11.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer11.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText24.Wrap( -1 )
		fgSizer11.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.save_button = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.save_button, 0, wx.ALL, 5 )
		
		self.edit_button = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"EDIT", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer11.Add( self.edit_button, 0, wx.ALL, 5 )
		
		self.reset_button = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"RESET", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.reset_button, 0, wx.ALL, 5 )
		
		
		sbSizer9.Add( fgSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.index_box.Bind( wx.EVT_CHOICE, self.selected_index )
		self.expiry_box.Bind( wx.EVT_CHOICE, self.selected_expiry_function )
		self.product_box.Bind( wx.EVT_CHOICE, self.selected_product )
		# self.save_button.Bind( wx.EVT_BUTTON, self.fetching_order_details )

		self.save_button.Bind( wx.EVT_BUTTON, self.on_lock_values)
		self.edit_button.Bind( wx.EVT_BUTTON, self.on_edit_values)
		self.reset_button.Bind(wx.EVT_BUTTON,self.on_reset_values)
		self.ce_strike.Bind( wx.EVT_TEXT, self.ce_ltp )
		self.pe_strike.Bind( wx.EVT_TEXT, self.pe_ltp )
		# self.ce_strike.Bind( wx.EVT_ENTER_WINDOW, self.ce_ltp )
		# self.ce_strike.Bind( wx.EVT_LEAVE_WINDOW, self.ce_ltp )
		# self.ce_strike = wx.TextCtrl(parent, style=wx.TE_PROCESS_ENTER)
		# self.ce_strike.Bind( wx.EVT_TEXT_ENTER, self.ce_ltp )
		self.current_index=None
		self.selected_expiry=None
		self.ce_high_ele = None
		self.ce_low_ele = None
		self.pe_high_ele = None
		self.pe_low_ele = None
		self.ce_start_time = None
		self.pe_start_time = None



		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.on_timer_function, self.timer)
		self.timer.Start(500)
	
	def __del__( self ):
		pass


	def set_broker_obj(self,all_expiries,map_dict,data_dict,smartApi,sws,exchange_token_hub,data_dict_exchng,contract_hub_exchng,mode,correlation_id,freeze_lotsize_dict):
		self.all_expiries = all_expiries
		self.map_dict=map_dict
		# self.kws=kws
		self.data_dict=data_dict
		self.smartApi=smartApi
		self.sws=sws
		self.exchange_token_hub=exchange_token_hub
		self.data_dict_exchng=data_dict_exchng
		self.contract_hub_exchng=contract_hub_exchng
		self.mode=mode
		self.correlation_id=correlation_id
		self.freeze_lotsize_dict=freeze_lotsize_dict
		self.selected_index(None)
		self.selected_expiry_function(None)
		logging.info("[+] Inside the main function")

	
	
	# Virtual event handlers, overide them in your derived class
	def selected_index( self, event ):
		# print(self.all_expiries)
		# print(self.contract_hub_exchng)
		current_index = self.index_box.GetStringSelection() 
		expiry_list = self.all_expiries[current_index]
		
		self.current_index=current_index

		self.expiry_box.SetItems(expiry_list)
		self.expiry_box.SetSelection(0)
		self.index_boxChoices = expiry_list

	def find_key_by_tradingsymbol(self,tradingsymbol):
		for token, details in self.contract_hub_exchng.items():
			if details['symbol'] == tradingsymbol:
				return token
		return None

	def get_key_from_name(self,name):
		'''This function will get the index name is map dict from user entered name'''
		# pass
		# print("name is ",name)
		for key,value in self.map_dict.items():
			if value['NAME'] == name:
				# print("key is", key )
				return key
		return None

	def find_trading_symbol_from_strike(self,index,expiry,strike):
		date_obj=datetime.strptime(expiry,"%Y-%m-%d")
		expiry_date=f"{date_obj.strftime("%d")}{date_obj.strftime("%b").upper()}{date_obj.strftime("%y")}"
		trading_symbol=f"{index}{expiry_date}{strike}"
		token=self.find_key_by_tradingsymbol(trading_symbol)
		if token is not None:
			return token

	def selected_expiry_function( self, event ):
		selected_expiry_tmp = self.expiry_box.GetStringSelection() 
		
		key=self.get_key_from_name(self.current_index)
		new_key=f"{key}_{selected_expiry_tmp}"	
		self.new_key=new_key	
		exchng_token=self.exchange_token_hub[new_key]
		combined_token= exchng_token['CE'] + exchng_token['PE']
		combined_token_str_list = [str(token) for token in combined_token]
		# print(combined_token_str_list)
		if self.current_index in ['BANKEX', 'SENSEX']:

	   		exchange_type = 4
		else:
			exchange_type = 2
		
		token_list = [
			{
				"action": 1,
				"exchangeType": exchange_type,
				"tokens": combined_token_str_list
			}
   			 ]
		self.sws.subscribe(self.correlation_id, self.mode, token_list)
		print(f"[+]  Subscribe Succefully")
	
	def selected_product( self, event ):
		pass
		#
	def on_lock_values(self, event):
		# Fetch user input values
		ce_value = self.ce_strike.GetValue() if self.ce_strike else None
		pe_value = self.pe_strike.GetValue() if self.pe_strike else None
		ce_stoploss = int(self.ce_sl.GetValue()) if self.ce_sl and self.ce_sl.GetValue().isdigit() else None
		ce_target = int(self.ce_target.GetValue()) if self.ce_target and self.ce_target.GetValue().isdigit() else None
		pe_stoploss = int(self.pe_sl.GetValue()) if self.pe_sl and self.pe_sl.GetValue().isdigit() else None
		pe_target = int(self.pe_target.GetValue()) if self.pe_target and self.pe_target.GetValue().isdigit() else None
		ce_qty_var = int(self.ce_qty.GetValue()) if self.ce_qty and self.ce_qty.GetValue().isdigit() else None
		pe_qty_var = int(self.pe_qty.GetValue()) if self.pe_qty and self.pe_qty.GetValue().isdigit() else None
		product_type = self.product_box.GetStringSelection()
		current_index_var = self.index_box.GetStringSelection() 
		product_box_var = self.product_box.GetStringSelection()
		start_time_str = self.time_box.GetValue()
		duration_minutes = self.timeframe_box.GetStringSelection()

		try:
			start_time = datetime.strptime(start_time_str, "%H.%M.%S").time()
		except ValueError:
			print("Please enter the start time in the format HH:MM:SS.")
			return 

		if not duration_minutes.isdigit():
			print("Please select a valid duration in minutes.")
			return  
		duration_minutes = int(duration_minutes)

		missing_values = []
		if ce_value is None:
			missing_values.append("CE Strike")
		if pe_value is None:
			missing_values.append("PE Strike")
		if ce_stoploss is None:
			missing_values.append("CE Stop Loss")
		if ce_target is None:
			missing_values.append("CE Target")
		if pe_stoploss is None:
			missing_values.append("PE Stop Loss")
		if pe_target is None:
			missing_values.append("PE Target")
		if ce_qty_var is None:
			missing_values.append("CE Quantity")
		if pe_qty_var is None:
			missing_values.append("PE Quantity")
		if not product_type:
			missing_values.append("Product Type")
		if not current_index_var:
			missing_values.append("Index")
		if not product_box_var:
			missing_values.append("Product Box")
		
		if missing_values:
			print(f"[+]  Please enter the following missing values: {', '.join(missing_values)}")
			return  # Exit the method if any values are missing

		# Disable input fields
		self.ce_strike.Disable()
		self.pe_strike.Disable()
		self.ce_sl.Disable()
		self.pe_sl.Disable()
		self.ce_target.Disable()
		self.pe_target.Disable()
		self.ce_qty.Disable()
		self.pe_qty.Disable()
		print("[+]  Click on save button ")
		logging.info("[+]  Click on save button ")
		ce_slice_qty=self.quantity_manage(current_index_var,ce_qty_var)
		pe_slice_qty=self.quantity_manage(current_index_var,pe_qty_var)
		print(f"[+]  Enter values are after save button --> Starttime : {start_time} Timeframe : {duration_minutes}min CE strike : {ce_value} CE Enter Qty : {ce_qty_var} CE Slice Qty : {ce_slice_qty} CE-Sl : {ce_stoploss} CE-Tgt : {ce_target}  PE strike : {pe_value} PE-Qty : {pe_qty_var} PE Slice Qty : {pe_slice_qty} PE-Sl : {pe_stoploss} PE-Tgt : {pe_target} ")
		logging.info(f"[+]  Enter values are after save button --> Starttime : {start_time} Timeframe : {duration_minutes}min CE strike : {ce_value} CE-Qty : {ce_qty_var} CE Slice Qty : {ce_slice_qty} CE-Sl : {ce_stoploss} CE-Tgt : {ce_target}  PE strike : {pe_value} PE-Qty : {pe_qty_var} PE Slice Qty : {pe_slice_qty} PE-Sl : {pe_stoploss} PE-Tgt : {pe_target} ")
		# Start the monitoring thread
		
		
		# print(f"CE Qty {ce_slice_qty}  PE Qty {pe_slice_qty}")
		thread = threading.Thread(target=self.monitor_ce_pe_ltp, args=(start_time_str, duration_minutes, self.get_ltp, ce_value, pe_value, ce_stoploss, ce_target, pe_stoploss, pe_target, ce_slice_qty, pe_slice_qty, product_type, product_box_var, current_index_var))
		thread.start()



	def on_edit_values(self,event):
		print("[+]  Click on edit button ")
		logging.info("[+]  Click on edit button ")
		self.ce_strike.Enable()
		self.pe_strike.Enable()
		self.ce_sl.Enable()
		self.pe_sl.Enable()
		self.ce_target.Enable()
		self.pe_target.Enable()
		self.ce_qty.Enable()
		self.pe_qty.Enable()

	def fetching_order_details( self, event ):
		pass
		# event.Skip()

	def on_timer_function(self, event):
		try:
			self.Update_CE_PE_ltp()
		except Exception as e:
			# print("Exception on_timer_function", e)
			pass

	# def get_ltp(self, strike_value, option_type):
	# 	current_index = self.index_box.GetStringSelection()
	# 	selected_expiry = self.expiry_box.GetStringSelection()

	# 	if not strike_value.upper().endswith(option_type):
	# 		strike_value += option_type

	# 	# Fetch the instrument token and trading symbol
	# 	fetch_token, trading_symbol = self.find_trading_symbol_from_strike(current_index, selected_expiry, strike_value)

	# 	if fetch_token is not None:
	# 		ltp = self.data_dict_exchng.get(str(fetch_token))
	# 		return {
	# 			"token": fetch_token,
	# 			"trading_symbol": trading_symbol,
	# 			"ltp": ltp
	# 		}

	# 	return None

	def get_ltp(self, strike_value, option_type):
		current_index = self.index_box.GetStringSelection()
		selected_expiry = self.expiry_box.GetStringSelection()
		if not strike_value.upper().endswith(option_type):
			strike_value += option_type
		
		fetch_token = self.find_trading_symbol_from_strike(current_index, selected_expiry, strike_value)
		if fetch_token is not None:
			return self.data_dict_exchng.get(str(fetch_token))
		return None

	def get_token_and_symbol(self, strike_value, option_type):
		current_index = self.index_box.GetStringSelection()
		selected_expiry = self.expiry_box.GetStringSelection()
		
		if not strike_value.upper().endswith(option_type):
			strike_value += option_type
		
		fetch_token = self.find_trading_symbol_from_strike(current_index, selected_expiry, strike_value)
		
		if fetch_token is not None:
			fetch_token_str = str(int(fetch_token))
			date_obj = datetime.strptime(selected_expiry, "%Y-%m-%d")
			expiry_date = f"{date_obj.strftime('%d')}{date_obj.strftime('%b').upper()}{date_obj.strftime('%y')}"
			trading_symbol = f"{current_index}{expiry_date}{strike_value.upper()}"
			
			return {
				"token": fetch_token_str,
				"trading_symbol": trading_symbol
			}
		
		return None


	
	def order_placement_function(self,token,trading_symbol,exchange,transaction_type,quantity,product_type,price):
		# print("inside order placement function")
		try:
			# print(f"Initial parameter values:")
			# print(f"trading_symbol: {trading_symbol} (type: {type(trading_symbol)})")
			# print(f"exchange: {exchange} (type: {type(exchange)})")
			# print(f"transaction_type: {transaction_type} (type: {type(transaction_type)})")
			# print(f"quantity: {quantity} (type: {type(quantity)})")
			# print(f"product_type: {product_type} (type: {type(product_type)})")
			# print(f"price: {price} (type: {type(price)})")

			for qty in quantity:
				token=str(token)
				trading_symbol = str(trading_symbol)
				exchange = str(exchange)
				transaction_type = str(transaction_type)
				new_quantity = int(qty)
				# print("After",new_quantity)
				product_type = str(product_type)
				# print("Product type",product_type)
				price = float(price)
				print(f"Placing order with params - trading_symbol: {trading_symbol}, exchange: {exchange}, "
				f"transaction_type: {transaction_type}, quantity: {new_quantity}, product_type: {product_type}, price: {price}")

				logging.info(f"[+]  Placing order with params - trading_symbol: {trading_symbol}, exchange: {exchange}, "
				f"transaction_type: {transaction_type}, quantity: {new_quantity}, product_type: {product_type}, price: {price}")

				if product_type == "MIS":
					product_type= "INTRADAY"
				else:
					product_type="CARRYFORWARD"
				orderparams = {
				"variety": "NORMAL",
				"tradingsymbol": trading_symbol,
				"symboltoken": token,
				"transactiontype": transaction_type,
				"exchange": exchange,
				"ordertype": "MARKET",
				"producttype": product_type,
				"duration": "DAY",
				"price": price,
				"quantity": new_quantity
				}
				orderid = self.smartApi.placeOrder(orderparams)
			# 	order_id = self.kite.place_order(tradingsymbol=trading_symbol,
			# 				exchange=exchange,
			# 				transaction_type=transaction_type,
			# 				quantity=quantity,
			# 				variety=self.kite.VARIETY_AMO,
			# 				order_type=self.kite.ORDER_TYPE_LIMIT,
			# 				product=product_type,
			# 				price=price,
			# 				validity=self.kite.VALIDITY_DAY)

				print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Order placed #{orderid}, Trading_symbol => {trading_symbol}, entry_price_when_order_get_executed => {price}")
				logging.info(f"[+]  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Order placed #{orderid}, Trading_symbol => {trading_symbol}, entry_price_when_order_get_executed => {price}")
		except Exception as e:
			print('Error occurred while placing order:', e)
			logging.info(f"[+]  Error occurred while placing order:{e}")

	def quantity_manage(self,current_index,quantity):
		lotsize_freeze_limits=self.freeze_lotsize_dict
		# print(lotsize_freeze_limits)
		lz=lotsize_freeze_limits[current_index]["lot_size"]
		fl=lotsize_freeze_limits[current_index]["freeze_limit"]
		x = int(quantity) // fl * [fl] + [((int(quantity)%fl) //lz ) * lz]
		return [i for i in x if i!=0]

	def exit_position(self, token, trading_symbol, quantity, exchange, product_type):
		"""
		Exits the position for a given token and trading symbol.
		
		Args:
			token (str): The token identifier for the option contract.
			trading_symbol (str): The trading symbol for the option contract.
			quantity (int): The quantity of the position to exit.
			exchange (str): The exchange on which the option is traded.
			product_type (str): The type of product (e.g., MIS, CNC).
		"""
		try:
			# Fetch the current positions to check if the position exists
			data = self.smartApi.position()
			trading_symbols = [item['tradingsymbol'] for item in data.get('data', [])]
			
			if trading_symbol in trading_symbols:
				# Place the sell order to exit the position
				for qty in quantity:
					self.order_placement_function(
						token=token,
						trading_symbol=trading_symbol,
						exchange=exchange,
						transaction_type="SELL",
						new_quantity=int(qty),
						product_type=product_type,
						price=0  # Market price
					)
					print(f"Exited position for {trading_symbol} with quantity {new_quantity}.")
					logging.info(f"[+]  Exited position for {trading_symbol} with quantity {new_quantity}")
			else:
				print(f"No matching trading symbol found for {trading_symbol}.")
				logging.info(f"[+]  No matching trading symbol found for {trading_symbol}.")
		
		except Exception as e:
			print(f"No matching trading symbol found for {trading_symbol}.")
			logging.info(f"[+]  No matching trading symbol found for {trading_symbol}.")
		

	def monitor_ce_pe_ltp(self, start_time_str, duration_minutes, get_ltp_func, ce_value, pe_value,ce_stoploss,ce_target, pe_stoploss, pe_target,ce_slice_qty,pe_slice_qty,product_type,product_box_var,current_index_var):
		try:
			start_time = datetime.strptime(start_time_str, "%H.%M.%S")
			if 1 <= start_time.hour <= 4:
				start_time = start_time.replace(hour=start_time.hour + 12)

			if current_index_var in ['NIFTY','BANKNIFTY','FINNIFTY',]:
				user_exchange="NFO"
			else:

				user_exchange="BFO"

			# print(f"CE Qty : {ce_slice_qty} PE Qty : {pe_slice_qty} ")

			start_datetime = datetime.combine(datetime.today(), start_time.time())
			end_datetime = start_datetime + timedelta(minutes=duration_minutes)
			# end_time = end_datetime.time()
			ce_high_ele = None
			ce_low_ele = None
			pe_high_ele = None
			pe_low_ele = None
			ce_status=None
			pe_status=None

			while True:
				current_time = datetime.now()

				if start_datetime <= current_time <= end_datetime:
					# Update CE values
					if ce_value:
						ltp_ce = get_ltp_func(ce_value, "CE")
						# print("ltp ce",type(ltp_ce))
						if ce_high_ele is None or ltp_ce > ce_high_ele:
							ce_high_ele = ltp_ce
							# print("Ce high",type(ce_high_ele))
						if ce_low_ele is None or ltp_ce < ce_low_ele:
							ce_low_ele = ltp_ce
							# print("ce_low",ce_low_ele)

					# Update PE values
					if pe_value:
						ltp_pe = get_ltp_func(pe_value, "PE")
						# print("ltp pe ", ltp_pe)
						if pe_high_ele is None or ltp_pe > pe_high_ele:
							pe_high_ele = ltp_pe
							
						if pe_low_ele is None or ltp_pe < pe_low_ele:
							pe_low_ele = ltp_pe
					time.sleep(1)

				elif current_time > end_datetime:
					print(f"Monitoring completed.")
					logging.info("[+]  Monitoring completed ")
					if ce_value:
						if ce_high_ele is not None and ce_low_ele is not None:
							print(f"CE High: {ce_high_ele:.2f}, CE Low: {ce_low_ele:.2f}")
							logging.info(f"[+]  CE High: {ce_high_ele:.2f}, CE Low: {ce_low_ele:.2f}")
							self.ce_high.SetLabel(str(ce_high_ele))
							self.ce_low.SetLabel(str(ce_low_ele))
							self.ce_status.SetLabel("Pending...!")
							font = self.ce_status.GetFont()
							font.SetWeight(wx.FONTWEIGHT_BOLD)
							self.ce_status.SetFont(font)
							self.ce_status.SetForegroundColour(wx.Colour(255, 0, 0))
						# print("ce_high_ele",type(ce_high_ele))
						# print(f"CE High: {ce_high_ele :2f}, CE Low: {ce_low_ele :2f}")
						# self.ce_high.SetLabel(str(ce_high_ele))
						# self.ce_low.SetLabel(str(ce_high_ele))
					if pe_value:
						if pe_high_ele is not None and pe_low_ele is not None:
							print(f"PE High: {pe_high_ele:.2f}, PE Low: {pe_low_ele:.2f}")
							logging.info(f"[+]  PE High: {pe_high_ele:.2f}, PE Low: {pe_low_ele:.2f}")
							self.pe_high.SetLabel(str(pe_high_ele))
							self.pe_low.SetLabel(str(pe_low_ele))
							self.pe_status.SetLabel("Pending...!")
							font = self.pe_status.GetFont()
							font.SetWeight(wx.FONTWEIGHT_BOLD)
							self.pe_status.SetFont(font)
							self.pe_status.SetForegroundColour(wx.Colour(255, 0, 0))
						
					break
				time.sleep(1)
				# print(f"PE High: {pe_high:.2f}, PE Low: {pe_low:.2f}")

			ce_info = self.get_token_and_symbol(ce_value, "CE") if ce_value else None
			pe_info = self.get_token_and_symbol(pe_value, "PE") if pe_value else None

			ce_token = ce_info["token"] if ce_info else None
			ce_trading_symbol = ce_info["trading_symbol"] if ce_info else None

			pe_token = pe_info["token"] if pe_info else None
			pe_trading_symbol = pe_info["trading_symbol"] if pe_info else None
			entry_price_ce = None
			entry_price_pe = None
			is_ce_entry_taken = False
			is_pe_entry_taken = False
			is_ce_exit_done=False
			is_pe_exit_done=False
			ce_exit_attempted = False  
			pe_exit_attempted = False 

			while True:
				ce_ltp=get_ltp_func(ce_value,"CE") if ce_value else None
				pe_ltp=get_ltp_func(pe_value,"PE") if pe_value else None

			
				# print(ce_ltp, ce_high_ele , is_ce_entry_taken)
				if ce_ltp and ce_ltp > ce_high_ele and not is_ce_entry_taken and not is_ce_exit_done:
					# print("ce elemet is high now")
					entry_price_ce=ce_ltp
					# below i need to check the data type of ltp and user enter value for stoploss
					system_ce_stoploss= entry_price_ce - ce_stoploss
					system_ce_target=entry_price_ce + ce_target
					self.ce_status.SetLabel("Entry Taken...!")
					font = self.ce_status.GetFont()
					font.SetWeight(wx.FONTWEIGHT_BOLD)
					self.ce_status.SetFont(font)
					self.ce_status.SetForegroundColour(wx.Colour(0, 128, 0))
					print(f"[+] CE high breakout ---> CE Entry Price: {entry_price_ce:.2f}, Stop Loss: {system_ce_stoploss:.2f}, Target: {system_ce_target:.2f}")
					logging.info(f"[+]  CE Entry Price: {entry_price_ce:.2f}, Stop Loss: {system_ce_stoploss:.2f}, Target: {system_ce_target:.2f}")
					self.order_placement_function(ce_token,ce_trading_symbol,exchange=user_exchange,transaction_type="BUY",quantity=ce_slice_qty,product_type=product_box_var,price=0)
					is_ce_entry_taken= True
					#  order placement logic start here
					# passs

				if pe_ltp and pe_ltp > pe_high_ele and not is_pe_entry_taken and not is_pe_exit_done:
					# order placmeent logic start here
					# print("ce elemet is high now")
					entry_price_pe=pe_ltp
					system_pe_stoploss=entry_price_pe - pe_stoploss
					system_pe_target=entry_price_pe + pe_target
					self.pe_status.SetLabel("Entry Taken...!")
					font = self.pe_status.GetFont()
					font.SetWeight(wx.FONTWEIGHT_BOLD)
					self.pe_status.SetFont(font)
					self.pe_status.SetForegroundColour(wx.Colour(0, 128, 0))
					print(f"[+]  PE high breakout ---> PE Entry Price: {entry_price_pe:.2f}, Stop Loss: {system_pe_stoploss:.2f}, Target: {system_pe_target:.2f}")
					logging.info(f"[+]  PE Entry Price: {entry_price_pe:.2f}, Stop Loss: {system_pe_stoploss:.2f}, Target: {system_pe_target:.2f}")
					# print(f"PE Token: {pe_token}, PE Trading Symbol: {pe_trading_symbol}")
					# print(f"Qty {pe_qty_var}  product : {product_type} price : {entry_price_pe}")
					self.order_placement_function(pe_token,pe_trading_symbol,exchange=user_exchange,transaction_type="BUY",quantity=pe_slice_qty,product_type=product_box_var,price=0)

					is_pe_entry_taken=True


				if ce_value and ce_ltp:
				# Handle CE stop-loss and target
					if is_ce_entry_taken and not ce_exit_attempted:
						if ce_ltp <= system_ce_stoploss or ce_ltp >= system_ce_target:
							try:
								if ce_ltp <= system_ce_stoploss:
									print(f"[+]  CE Stop-Loss Hit: {ce_ltp:.2f}, Exiting Position.")
									logging.info(f"[+]  CE Stop-Loss Hit: {ce_ltp:.2f}, Exiting Position.")
								elif ce_ltp >= system_ce_target:
									print(f"[+]  CE Target Hit: {ce_ltp:.2f}, Exiting Position.")
									logging.info(f"[+]  CE Target Hit: {ce_ltp:.2f}, Exiting Position.")
								if ce_token and ce_trading_symbol:
									self.ce_status.SetLabel("Exit Attempted...!")
									self.exit_position(ce_token, ce_trading_symbol, ce_slice_qty, user_exchange, product_type)
								is_ce_exit_done = True
								ce_exit_attempted = True
							except Exception as e:
								print(f"[+]  An error occurred while exiting the position for {ce_trading_symbol}: {str(e)}")
								logging.info(f"[+]  An error occurred while exiting the position for {ce_trading_symbol}: {str(e)}")


				if pe_value and pe_ltp:
				# Handle PE stop-loss and target
					if is_pe_entry_taken and not pe_exit_attempted:
						if pe_ltp <= system_pe_stoploss or pe_ltp >= system_pe_target:
							try:
								if pe_ltp <= system_pe_stoploss:
									print(f"[+]  PE Stop-Loss Hit: {pe_ltp:.2f}, Exiting Position.")
									logging.info(f"[+]  PE Stop-Loss Hit: {pe_ltp:.2f}, Exiting Position.")
								elif pe_ltp >= system_pe_target:
									print(f"[+]  PE Target Hit: {pe_ltp:.2f}, Exiting Position.")
									logging.info(f"[+]  PE Target Hit: {pe_ltp:.2f}, Exiting Position.")
								if pe_token and pe_trading_symbol:
									self.pe_status.SetLabel("Exit Attempted...!")
									self.exit_position(pe_token, pe_trading_symbol, ce_slice_qty, user_exchange, product_type)
								# is_pe_entry_taken = False
								is_pe_exit_done = True
								pe_exit_attempted = True
							except Exception as e:
								print(f"[+]  An error occurred while exiting the position for {pe_trading_symbol}: {str(e)}")	
								logging.info(f"[+]  An error occurred while exiting the position for {pe_trading_symbol}: {str(e)}")

				if (is_ce_exit_done or not ce_value) and (is_pe_exit_done or not pe_value):
					break
				time.sleep(1)
		except Exception as e:
			pass

	def Update_CE_PE_ltp(self):
		ce_value = self.ce_strike.GetValue()
		if ce_value:
			ltp = self.get_ltp(ce_value, "CE")
			self.ce_ltp_.SetLabel(str(ltp))
			# self.ce_ltp_.SetLabel(str(f"{(format(ltp_, '.2f'))}"))
		# Update PE values
		pe_value = self.pe_strike.GetValue()
		if pe_value:
			ltp = self.get_ltp(pe_value, "PE")
			self.pe_ltp_.SetLabel(str(ltp))


	

	def ce_ltp( self, event ):
		current_index = self.index_box.GetStringSelection() 
		ce_value = self.ce_strike.GetValue()
		selected_expiry = self.expiry_box.GetStringSelection() 
		if not ce_value.upper().endswith("CE"):
			ce_value += "CE"
			fetch_token=self.find_trading_symbol_from_strike(current_index,selected_expiry,ce_value)
			if fetch_token is not None:
				# print("fetch token is ",fetch_token)
				ltp_=self.data_dict_exchng[str(fetch_token)]
				self.ce_ltp_.SetLabel(str(f"{(format(ltp_, '.2f'))}"))
				# print("ltp is ",ltp_)
				# print(sws.on_ticks)
				

	def pe_ltp( self, event ):
		current_index = self.index_box.GetStringSelection() 
		pe_value = self.pe_strike.GetValue()
		selected_expiry = self.expiry_box.GetStringSelection() 
		if not pe_value.upper().endswith("PE"):
			pe_value += "PE"
			fetch_token=self.find_trading_symbol_from_strike(current_index,selected_expiry,pe_value)
			if fetch_token is not None:
				# print("fetch token is ",fetch_token)
				ltp_=self.data_dict_exchng[str(fetch_token)]
				self.pe_ltp_.SetLabel(str(ltp_))
				# print("ltp is ",ltp_)

	def is_time_reached(self,time,after_how_many_min):
		hr,min,sec=map(int,time.split("."))
		current_time=datetime.now()
		user_time=current_time.replace(hour=hr,minute=min,second=sec)
		target_time=user_time + timedelta(minutes=int(after_how_many_min))
		while True:
			current_time = datetime.now()
			if current_time > target_time:
				print(f"[+]  Time exceeded at {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
				logging.info("[+]  Time exceeded at {current_time.strftime('%Y-%m-%d %H:%M:%S')} ")
				break

	def on_reset_values(self, event):
			"""
			Resets all input fields to their default state and enables them.
			"""
			try:
				print("[+]  Click on reset button")
				logging.info("[+]  Click on reset button ")

				self.ce_strike.SetValue("")
				self.pe_strike.SetValue("")
				self.ce_sl.SetValue("")
				self.pe_sl.SetValue("")
				self.ce_target.SetValue("")
				self.pe_target.SetValue("")
				self.ce_qty.SetValue("")
				self.pe_qty.SetValue("")
				# self.product_box.SetSelection(-1)
				# self.index_box.SetSelection(-1)
				self.time_box.SetValue("")
				# self.timeframe_box.SetSelection(-1)

				# Enable input fields
				self.ce_strike.Enable()
				self.pe_strike.Enable()
				self.ce_sl.Enable()
				self.pe_sl.Enable()
				self.ce_target.Enable()
				self.pe_target.Enable()
				self.ce_qty.Enable()
				self.pe_qty.Enable()

				self.ce_value = None
				self.pe_value = None
				self.ce_qty_var = None
				self.pe_qty_var = None
				self.ce_stoploss = None
				self.pe_stoploss = None
				self.ce_target = None
				self.pe_target = None
				self.ce_status = None
				self.pe_status = None
				# self.ce_status.SetLabel("")
				# self.pe_status.SetLabel("")
				# self.ce_ltp_.SetLabel("")
				self.ce_ltp_.SetLabel("")
				self.pe_ltp_.SetLabel("")
			except Exception as e:
				pass	
		# self.ce_ltp_.GetLabel()
		