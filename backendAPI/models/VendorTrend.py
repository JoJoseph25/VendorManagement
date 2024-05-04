from uuid import uuid4
from datetime import datetime
from configs.extensions import dbModel

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

class VendorTrend(dbModel):
    __tablename__ = "vendor_trend"

    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    vendor: Mapped[uuid4] = mapped_column(ForeignKey("vendors.vendor_code", ondelete="CASCADE"), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.now)
    quality_rating_avg: Mapped[float] = mapped_column(nullable=False, default=0.0)
    average_response_time: Mapped[float] = mapped_column(nullable=False, default=0.0)
    fulfillment_rate: Mapped[float] = mapped_column(nullable=False, default=0.0)

    def __init__(self, **kwargs):
        super(VendorTrend, self).__init__(**kwargs)

    def __repr__(self):
        return f'<VendorTrend {self.vendor.hex}[{self.date}]>'
    
    # def db_write(self):
    #     db.session.add(self)
        # db.session.commit()