from uuid import uuid4
from typing import List, Optional
from configs.extensions import dbModel

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Vendors(dbModel):
    __tablename__ = "vendors"

    vendor_code: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(264), nullable=False)
    contact_details: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    on_time_delivery_rate: Mapped[float] = mapped_column(nullable=False, default=100.0)
    quality_rating_avg: Mapped[float] = mapped_column(nullable=False, default=100.0)
    average_response_time: Mapped[float] = mapped_column(nullable=False, default=100.0)
    fulfillment_rate: Mapped[float] = mapped_column(nullable=False, default=100.0)
    po_orders: Mapped[List['PurchaseOrders']] = relationship(backref='vendors')


    def __init__(self, **kwargs):
        super(Vendors, self).__init__(**kwargs)

    def __repr__(self):
        return f'<Vendor {self.name}[{self.id.hex}]>'
    
    # def db_write(self):
    #     db.session.add(self)
        # db.session.commit()